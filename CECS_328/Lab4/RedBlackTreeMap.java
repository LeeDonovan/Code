import java.util.*;

import javax.swing.plaf.nimbus.NimbusLookAndFeel;

// A Map ADT structure using a red-black tree, where keys must implement
// Comparable.
// The key type of a map must be Comparable. Values can be any type.
public class RedBlackTreeMap<TKey extends Comparable<TKey>, TValue> {
	// A Node class.
	private class Node {
		private TKey mKey;
		private TValue mValue;
		private Node mParent;
		private Node mLeft;
		private Node mRight;
		private boolean mIsRed;

		// Constructs a new node with NIL children.
		public Node(TKey key, TValue data, boolean isRed) {
			mKey = key;
			mValue = data;
			mIsRed = isRed;

			mLeft = NIL_NODE;
			mRight = NIL_NODE;
		}

		@Override
		public String toString() {
			return mKey + " : " + mValue + " (" + (mIsRed ? "red)" : "black)");
		}
	}

	private Node mRoot;
	private int mCount;

	// Rather than create a "blank" black Node for each NIL, we use one shared
	// node for all NIL leaves.
	private final Node NIL_NODE = new Node(null, null, false);

	//////////////////// I give you these utility functions for free.

	// Get the # of keys in the tree.
	public int getCount() {
		return mCount;
	}

	// Finds the value associated with the given key.
	public TValue find(TKey key) {
		Node n = bstFind(key, mRoot); // find the Node containing the key if any
		if (n == null || n == NIL_NODE)
			throw new RuntimeException("Key not found");
		return n.mValue;
	}

	/////////////////// You must finish the rest of these methods.

	// Inserts a key/value pair into the tree, updating the red/black balance
	// of nodes as necessary. Starts with a normal BST insert, then adjusts.
	public void add(TKey key, TValue data) {
		Node n = new Node(key, data, true); // nodes start red

		// normal BST insert; n will be placed into its initial position.
		// returns false if an existing node was updated (no rebalancing needed)
		boolean insertedNew = bstInsert(n, mRoot);
		if (!insertedNew)
			return;

		// check cases 1-5 for balance violations.
		checkBalance(n);
	}

	// Applies rules 1-5 to check the balance of a tree with newly inserted
	// node n.
	private void checkBalance(Node n) {
		Node x = n;
		Node gramps = getGrandparent(x);
		Node uncle = getUncle(x);
		if (x == mRoot) {
			// case 1: new node is root
			x.mIsRed = false;
			return;
		}
		// handle additional insert cases here.
		// case 2
		if(!x.mParent.mIsRed){
			return;
		}
		//case 3
		if(uncle.mIsRed){
			x.mParent.mIsRed = false;
			uncle.mIsRed = false;
			gramps.mIsRed = true;
			checkBalance(gramps);//recursion
		}
		else{
			//case 4
			if(x == x.mParent.mRight && x.mParent == gramps.mLeft){
				singleRotateLeft(n.mParent);
				x = x.mLeft;
			}
			else if(x == x.mParent.mLeft && x.mParent == gramps.mRight){
				singleRotateRight(n.mParent);
				x = x.mRight;
			}
			//case 5
			if(x == gramps.mLeft.mLeft){
				gramps.mIsRed = true;
				x.mParent.mIsRed = false;
				singleRotateRight(gramps);
			}
			if(n == gramps.mRight.mRight){
				gramps.mIsRed = true;
				x.mParent.mIsRed = false;
				singleRotateLeft(gramps);
			}

		}
		

	}

	// Returns true if the given key is in the tree.
	public boolean containsKey(TKey key) {
		// TODO: using at most three lines of code, finish this method.
		// HINT: write the bstFind method first.
		Node x = bstFind(key, mRoot);
		if(x == null){
			return false;
		}
		if(x.mKey == key){
			return true;
		}
		return false;
	}

	// Prints a pre-order traversal of the tree's nodes, printing the key, value,
	// and color of each node.
	public void printStructure() {
		// TODO: a pre-order traversal. Will need recursion.
		
		preOrder(mRoot);
	}
	private void preOrder(Node n){
		if( n == NIL_NODE){
			return;
		}
		System.out.println(n.toString() + " | ");

		preOrder(n.mLeft);
		
		preOrder(n.mRight);
		
	}

	// Returns the Node containing the given key. Recursive.
	private Node bstFind(TKey key, Node currentNode) {
		// TODO: write this method. Given a key to find and a node to start at,
		// proceed left/right from the current node until finding a node whose
		// key is equal to the given key.
	
		if(currentNode == NIL_NODE || currentNode.mKey.equals(key)){
			return currentNode;
		}
		if(currentNode.mKey.compareTo(key) >= 0){
			return bstFind(key, currentNode.mLeft);
		}
		return bstFind(key, currentNode.mRight);
	}
	public boolean checkNILs(TKey key){
		Node x = bstFind(key, mRoot);
		if(x.mKey.equals(key)){
			if(x.mLeft == NIL_NODE && x.mRight == NIL_NODE){
				return true;
			}
			else{
				return false;
			}
		}
		else{
			return false;
		}
	}

	public boolean halfNHalf(TKey key){
		Node x = bstFind(key, mRoot);
		if(x.mKey.equals(key)){
			if((x.mLeft == NIL_NODE && x.mRight != NIL_NODE) || (x.mLeft != NIL_NODE && x.mRight == NIL_NODE)){
				return true;
			}
			else{
				return false;
			}
		}
		else{
			return false;
		}
	}
	public boolean reddyOrNot(TKey key){
		Node x = bstFind(key, mRoot);
		if(x.mKey.equals(key)){
			if(x.mIsRed){
				return true;
			}
			else{
				return false;
			}
		}
		else{
			return false;
		}
	}

	public TKey getKey(){
		return mRoot.mKey;
	}


	//////////////// These functions are needed for insertion cases.

	// Gets the grandparent of n.
	private Node getGrandparent(Node n) {
		// TODO: return the grandparent of n
		if(n != null && n.mParent != null){
			return n.mParent.mParent;
		}
		else{
			return null;
		}
		
	}

	// Gets the uncle (parent's sibling) of n.
	private Node getUncle(Node n) {
		// TODO: return the uncle of n
		Node gp = getGrandparent(n);
		if(gp == null || gp == NIL_NODE){
			return null;
		}
		if(gp.mLeft == n.mParent){
			return gp.mRight;
		}

		return gp.mLeft;
		
	}

	// Rotate the tree right at the given node.
	private void singleRotateRight(Node n) {
		Node l = n.mLeft; 
		Node lr = l.mRight; 
		Node p = n.mParent;
		n.mLeft = lr;
		lr.mParent = n;
		l.mRight = n;
		n.mParent = l;

		if (p == null) { // n is root
			mRoot = l;
		}
		else if (p.mLeft == n) {
			p.mLeft = l;
		} 
		else {
			p.mRight = l;
		}
		
		l.mParent = p;
	}

	// Rotate the tree left at the given node.
	private void singleRotateLeft(Node n) {
		// TODO: do a single left rotation (AVL tree calls this a "rr" rotation)
		// at n.
		Node r = n.mRight;
		Node rr = r.mLeft;
		Node p = n.mParent;
		n.mRight = rr;
		rr.mParent = n;
		r.mLeft = n;
		n.mParent = r;

		if(p == null){
			mRoot = r;
		}
		else if(p.mRight == n){
			p.mRight = r;
		}
		else{
			p.mLeft = r;
		}
		r.mParent = p;
	}


	// This method is used by insert. It is complete.
	// Inserts the key/value into the BST, and returns true if the key wasn't
	// previously in the tree.
	private boolean bstInsert(Node newNode, Node currentNode) {
		if (mRoot == null) {
			// case 1
			mRoot = newNode;
			return true;
		} 
		else {
			int compare = currentNode.mKey.compareTo(newNode.mKey);
			if (compare < 0) {
				// newNode is larger; go right.
				if (currentNode.mRight != NIL_NODE) {
					return bstInsert(newNode, currentNode.mRight);
				}
				else {
					currentNode.mRight = newNode;
					newNode.mParent = currentNode;
					mCount++;
					return true;
				}
			} 
			else if (compare > 0) {
				if (currentNode.mLeft != NIL_NODE) {
					return bstInsert(newNode, currentNode.mLeft);
				}
				else {
					currentNode.mLeft = newNode;
					newNode.mParent = currentNode;
					mCount++;
					return true;
				}
			} 
			else {
				// found a node with the given key; update value.
				currentNode.mValue = newNode.mValue;
				return false; // did NOT insert a new node.
			}
		}
	}
}
