import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import precision_recall_curve, accuracy_score, precision_score, recall_score, f1_score
import numpy as np
import pandas as pd

# 데이터 로드 및 전처리
full_df3 = con_df.copy()
full_df3['REVIEW_TIME'] = pd.to_datetime(full_df3['REVIEW_TIME'])
full_df3['REVIEW_TIMESTAMP'] = full_df3['REVIEW_TIME'].apply(lambda x: x.timestamp())

# 피처와 레이블 설정
features = full_df3[['SHOP_ID', 'CUST_ID', 'REVIEW_RANK', 'REVIEW_TIMESTAMP']].values
labels = full_df3['LABEL'].values  # 실제 레이블

# 데이터 정규화 (MinMaxScaler 사용)
scaler = MinMaxScaler()
features_scaled = scaler.fit_transform(features)

# PyTorch 텐서로 변환
data = torch.tensor(features_scaled, dtype=torch.float32)
labels_tensor = torch.tensor(labels, dtype=torch.int64)

# DataLoader로 변환
batch_size = 16
dataset = TensorDataset(data)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# AutoEncoder 모델 정의
class Autoencoder(nn.Module):
    def __init__(self, input_dim, encoding_dim):
        super(Autoencoder, self).__init__()
        # Encoder
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.LeakyReLU(),
            nn.Dropout(0.2),  # 드롭아웃 비율 조정
            nn.Linear(128, encoding_dim),
            nn.LeakyReLU()
        )
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(encoding_dim, 128),
            nn.LeakyReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, input_dim),
            nn.Sigmoid()  # 입력 데이터가 [0, 1]로 정규화되어 있다고 가정
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

# 모델 인스턴스 생성
input_dim = data.shape[1]  # 입력 데이터의 차원 (SHOP_ID, CUST_ID, REVIEW_RANK, REVIEW_TIMESTAMP)
encoding_dim = 5  # 인코딩 차원
model = Autoencoder(input_dim, encoding_dim)

# 손실 함수와 옵티마이저 정의
criterion = nn.HuberLoss()  # HuberLoss 사용
optimizer = optim.Adam(model.parameters(), lr=0.0005)  # 학습률 조정

# Early Stopping 설정
best_loss = float('inf')
patience = 10  # patience 설정 (연속적으로 개선되지 않으면 학습을 중단)
trigger_times = 0

# 모델 학습
num_epochs = 100

for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for batch in dataloader:
        inputs = batch[0]

        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, inputs)

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    epoch_loss = running_loss / len(dataloader)
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {epoch_loss:.4f}')

    # Early Stopping 체크
    if epoch_loss < best_loss:
        best_loss = epoch_loss
        trigger_times = 0
    else:
        trigger_times += 1
        if trigger_times >= patience:
            print("Early stopping activated.")
            break

# 이상 탐지
model.eval()

# 모든 데이터를 사용하여 재구성 오류 계산
with torch.no_grad():
    reconstructed = model(data)
    reconstruction_error = torch.mean((data - reconstructed) ** 2, dim=1).numpy()

# Precision-Recall 커브를 사용한 임계값 선택
precision, recall, thresholds = precision_recall_curve(labels, reconstruction_error)

# NaN 방지: 0으로 나눌 때 발생하는 에러 방지
f1_scores = np.divide(2 * (precision * recall), (precision + recall), where=(precision + recall) != 0)
f1_scores = np.nan_to_num(f1_scores)  # NaN을 0으로 변환

# 최적의 임계값 선택
best_threshold_index = np.argmax(f1_scores)
best_threshold = thresholds[best_threshold_index]
best_f1 = f1_scores[best_threshold_index]

# 임계값 적용
predicted_anomalies = (reconstruction_error > best_threshold).astype(int)

# 평가 지표 계산
accuracy = accuracy_score(labels, predicted_anomalies)
precision = precision_score(labels, predicted_anomalies)
recall = recall_score(labels, predicted_anomalies)
f1 = f1_score(labels, predicted_anomalies)

# 결과 출력
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"Best Threshold: {best_threshold}")

# 예측 결과를 원본 데이터에 추가
full_df3['p_auto_pred'] = predicted_anomalies
