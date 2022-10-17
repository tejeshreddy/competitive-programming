class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count = collections.Counter(sentence)
        return len(count) == 26
        