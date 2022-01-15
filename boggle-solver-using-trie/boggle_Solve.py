class TrieNode: 
      
    # Trie node class 
    def __init__(self): 
        self.children = [None]*26

        self.isEndOfWord = False
        self.word  = []
  
class Trie: 
       
    # Trie data structure class 
    def __init__(self): 
        self.root = self.getNode() 
  
    def getNode(self): 

        return TrieNode() 
  
    def _charToIndex(self,ch): 

          
        return ord(ch)-ord('a') 
  
  
    def insert(self,key): 

        root = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 

            try:
            	if not root.children[index]: 
                	root.children[index] = self.getNode()
            	root = root.children[index]
            except:
            	pass

  
        # mark last node as leaf 
        root.isEndOfWord = True
        root.word = word


file = open('engmix.txt',errors = 'ignore')

dictionary = []

for word in file:

	if len(word) < 4:
		continue

	dictionary.append(word[:-1])



trie = Trie()
for word in dictionary:
	trie.insert(str(word))

solutions = list()

def solve(board,i,j,r,c,curr):

	index = ord(board[i][j]) - ord('a')

	if board[i][j] == '$' or curr.children[index] == None:
		return

	curr = curr.children[index]

	if curr.isEndOfWord:
		solutions.append(curr.word)
		curr.isEndOfWord = False

	ch = board[i][j]
	board[i][j] = '$'

	if i > 0:
		solve(board, i - 1, j, r, c, curr)

	if i < r - 1:
		solve(board, i + 1, j, r, c, curr)

	if j > 0:
		solve(board, i, j - 1, r, c, curr)

	if j < c - 1 :
		solve(board, i, j + 1, r, c, curr)

	if i<r-1 and j < c-1:
		solve(board, i+1, j + 1, r, c, curr)

	if i > 0 and j>0:
		solve(board, i-1, j - 1, r, c, curr)

	if i>0 and j<c-1:
		solve(board, i-1, j + 1, r, c, curr)
		
	if i<r-1 and j>0:
		solve(board, i+1, j -1, r, c, curr)


	board[i][j] = ch

def findWords(board):
	make_lower_case(board)
	r = len(board)
	c = len(board[0])

	for i in range(r):
		for j in range(c):
			solve(board,i,j,r,c,trie.root)

	return solutions


def make_lower_case(mat):

	length = len(mat[0])

	for row in range(length):
		for col in range(length):
			mat[row][col] = mat[row][col].lower()
			
if __name__ == "__main__":


	board = \
	[['s', 't'], 
	 ['p', 'o']]


	print(findWords(board))




 


