#include <bits/stdc++.h>
using namespace std;

class trie
{
public:
	trie *child[26];
	bool endofword;
	string word;
};

trie* newnode()
{
	trie *node  = new trie;
	node->endofword = false;
	node->word = "";
	fr(i, 0, 25)
	{
		node->child[i] = NULL;
	}

	return node;
}

void insert(trie *root, string key)
{
	trie *p = root;
	fr(i, 0, key.length())
	{
		int index = key[i] - 'a';
		if (!p->child[index])
			p->child[index] = newnode();

		p = p->child[index];
	}
	p->endofword = true;
	p->word = key;
}

void solve(vector<vector<char>>& board, int i, int j, int r, int c, vector<string>& ans, trie *curr)
{
	//Base case
	//If the trie doesn't have the current char OR cell is Visited
	int index = board[i][j] - 'a';
	if (board[i][j] == '$' || curr->child[index] == NULL)
		return;

	curr = curr->child[index];
	if (curr->endofword)
	{
		ans.push_back(curr->word);
		curr->endofword = false;
	}

	//Body
	char ch = board[i][j];   //Store current char
	board[i][j] = '$';  //Mark current node visited

	if (i > 0)  //TOP
		solve(board, i - 1, j, r, c, ans, curr);
	if (i < r - 1) //DOWN
		solve(board, i + 1, j, r, c, ans, curr);
	if (j > 0)  //LEFT
		solve(board, i, j - 1, r, c, ans, curr);
	if (j < c - 1) //RIGHT
		solve(board, i, j + 1, r, c, ans, curr);

	board[i][j] = ch;    //Mark current node as Unvisited by restoring the value
}


vector<string> findWords(trie* root, vector<vector<char>>& board, vector<string>& words) {
	int r = board.size();
	int c = board[0].size();

	//Insert all words in TRIE
	for (int i = 0; i < words.size(); ++i)
		insert(root, words[i]);

	//Now search words
	vector<string> ans;
	for (int i = 0; i < r; ++i)
	{
		for (int j = 0; j < c; ++j)
			solve(board, i, j, r, c, ans, root);
	}
	return ans;
}

int main()
{

	IOS;

	vector<string> v {"the", "algo", "there", "answer",
	                  "any", "by", "bye", "their", "stop", "top", "sop"};

	vector<vector<char>> grid {{'s', 't'},
		{'p', 'o'}};

	trie *root = newnode();

	vector<string> anss = findWords(root, grid, v);

	for (auto i : anss)
	{
		cout << i << " ";
	}

	return 0;

}