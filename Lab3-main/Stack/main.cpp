#include <iostream>

using namespace std;

struct Node{

    int data;
    Node* link;

};

Node* topElement;
int top;
int Size = 5;

void push(int data){

    Node* temp = new Node();

    if(top>(Size)){
        cout<<"Stack is full"<<endl;
        exit(1);
    }
    else{
        top++;
        temp -> data = data;
        temp -> link = topElement;
        topElement = temp;

    }


}

bool isEmpty(){

    if(topElement == NULL){

        return true;
    }
    else{

        return false;
    }

}

int peek(){

    if(!isEmpty()){

        return topElement -> data;
    }
    else{
        cout<<"Stack is empty"<<endl;
        exit(1);
    }
}

void pop(){

    Node* temp;

    if(topElement == NULL){
        exit(1);
    }
    else{
        top--;
        temp = topElement;
        topElement = topElement -> link;
        free(temp);
        cout<<"Node deleted"<<endl;
    }
}

void print(){

    Node* temp;

    if(topElement == NULL){
        exit(1);
    }
    else{
        temp = topElement;

        while(temp != NULL){

            cout<<temp -> data<<" ";

            temp = temp -> link;
        }
        cout<<endl;
    }
}
int main()
{
    push(5);
    push(10);
    push(12);
    push(7);
    push(5);

    cout<<"Push:";
    print();

    cout<<"Top element is "<<peek()<<endl;

    pop();

    peek();

    push(5);
    push(6);
    push(9);
    peek();




}
