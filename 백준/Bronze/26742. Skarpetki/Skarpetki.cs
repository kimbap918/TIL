namespace Solution {
  class Program {
    static void Main(string[] args) {

      var input = Console.ReadLine()!;

      int whiteSocks = 0, blackSocks = 0;

      foreach (char c in input) {
        if (c == 'B') whiteSocks++;
        else blackSocks++;
      }

      int pairs = whiteSocks / 2 + blackSocks / 2;
      Console.WriteLine(pairs);

    }
  }
}