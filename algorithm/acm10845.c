#include<stdio.h>
#include<stdlib.h>

typedef struct{
  int front;
  int rear;
  int* que;
} Queue;

int Initialize(Queue* q){
  int front = 0;
  int rear = 0;
  if((q->que = (int* )calloc(10000,sizeof(int)))==NULL)
    return-1;
  return 0;
}

void push(Queue* q,int x){
  q->que[q->rear++]=x;
}

int pop(Queue* q){
  if(q->front==q->rear)
    return -1;
  else
    return q->que[q->front++];
}

int size(Queue* q){
  return q->rear - q->front;
}

int empty(Queue* q){
  if(q->front==q->rear)
    return 1;
  else
    return 0;
}

int front(Queue* q){
  if(q->front==q->rear)
    return -1;
  else
    return q->que[q->front];
}

int back(Queue* q){
    if(q->front==q->rear)
      return -1;
    else
      return q->que[q->rear-1];
}

int answer(Queue* q,char* s){

  if(strcmp(s,"pop")==0){
    return pop(q);
  }
  if(strcmp(s,"size")==0){
    return size(q);
  }
  if(strcmp(s,"empty")==0){
    return empty(q);
  }
  if(strcmp(s,"front")==0){222
    return front(q);
  }
  if(strcmp(s,"back")==0){
    return back(q);
  }
  return -1;
}

int main(void){

  Queue* queue;
  Initialize(queue);

  int n;
  scanf("%d",&n);

  int i;
  int x;
  char* s;
  for(i=0;i<n;i++){
    scanf("%s %d",&s,&x);
    if(strcmp(&s,"push"))
      push(queue,x);
    else{
      printf("%d\n",answer(queue,s));
    }
  }

  return 0;
}
