#include <bits/stdc++.h>

using namespace std;

template<class T>
struct ListNode
{
	T data;
	ListNode<T>* nextPtr;
};

// -------------------------------------------------------------------------------- insert

template<class T>
void insert( T** sPtr, auto value )
{ 
	T* newPtr; // pointer to new node
	T* previousPtr; // pointer to previous node in list
	T* currentPtr; // pointer to current node in list

	newPtr = new T(); // create node

	if ( newPtr != NULL ) { // is space available
		newPtr->data = value; // place value in node
		newPtr->nextPtr = NULL; // node does not link to another node

		previousPtr = NULL;
		currentPtr = *sPtr;

		// loop to find the correct location in the list       
		while ( currentPtr != NULL && value > currentPtr->data ) {
			previousPtr = currentPtr; // walk to ...               
			currentPtr = currentPtr->nextPtr; // ... next node 
		} // end while                                         

		// insert new node at beginning of list
		if ( previousPtr == NULL ) { 
			newPtr->nextPtr = *sPtr;
			*sPtr = newPtr;
		} // end if
		else { // insert new node between previousPtr and currentPtr
			previousPtr->nextPtr = newPtr;
			newPtr->nextPtr = currentPtr;
		} // end else
	} // end if
	else {
		printf( "%c not inserted. No memory available.\n", value );
	} // end else
} // end function insert

// -------------------------------------------------------------------------------- delete

template<class T>
char del( T** sPtr, auto value )
{ 
	T* previousPtr; // pointer to previous node in list
	T* currentPtr; // pointer to current node in list
	T* tempPtr; // temporary node pointer

	// delete first node
	if ( value == ( *sPtr )->data ) { 
		tempPtr = *sPtr; // hold onto node being removed
		*sPtr = ( *sPtr )->nextPtr; // de-thread the node
		free( tempPtr ); // free the de-threaded node
		return value;
	} // end if
	else { 
		previousPtr = *sPtr;
		currentPtr = ( *sPtr )->nextPtr;

		// loop to find the correct location in the list
		while ( currentPtr != NULL && currentPtr->data != value ) { 
			previousPtr = currentPtr; // walk to ...  
			currentPtr = currentPtr->nextPtr; // ... next node  
		} // end while

		// delete node at currentPtr
		if ( currentPtr != NULL ) { 
			tempPtr = currentPtr;
			previousPtr->nextPtr = currentPtr->nextPtr;
			free( tempPtr );
			return value;
		} // end if
	} // end else

	return '\0';
} // end function delete

// -------------------------------------------------------------------------------- isEmpty

template<class T>
int isEmpty( T* sPtr )
{ 
	return sPtr == NULL;
} // end function isEmpty

// -------------------------------------------------------------------------------- printList

template<class T>
void printList( T* currentPtr )
{ 
	// if list is empty
	if ( isEmpty<T>( currentPtr ) ) {
		puts( "List is empty.\n" );
	} // end if
	else { 
		puts( "The list is:" );

		// while not the end of the list
		while ( currentPtr != NULL ) { 
			cout << currentPtr->data << " --> ";
			currentPtr = currentPtr->nextPtr;   
		} // end while

		puts( "NULL\n" );
	} // end else
} // end function printList



// -------------------------------------------------------------------------------- nodeWrapper



template<class T>
class nodeWrapper: public iterator<input_iterator_tag, T>
{
public:
	nodeWrapper(T* p = NULL): ptr(p) {};

	auto operator*()
	{
		return ptr->data;
	}

	nodeWrapper& operator++()
	{
		ptr = ptr->nextPtr;
		return *this;
	}

	bool operator!=(const nodeWrapper& r) const
	{
		return ptr != r.ptr;
	}

private:
	T* ptr;
};



// -------------------------------------------------------------------------------- MAIN



int main(int argc, char const *argv[])
{
	ListNode<char>* head = NULL;

	for(int i='a'; i<'g'; i++)
		insert<ListNode<char> >(&head, i);

	nodeWrapper<ListNode<char> > it_begin(head);
	nodeWrapper<ListNode<char> > it_end;

	cout << *find(it_begin, it_end, 'b') << '\n';

	return 0;
}