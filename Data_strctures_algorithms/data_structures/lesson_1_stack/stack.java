/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

// public class Main
// {
// 	public static void main(String[] args) {
// 		System.out.println("Hello World");
// 	}
// }

public class Stack {
    private int[] array;
    private int count;
    private int size;
    
    public Stack(int siz) {
        array = new int[siz];
        size = siz;
        count=0;
    }
    
    public boolean isEmpty() {
        if (count==0) return true;
        return false;
    }

    
    public void push(int num){
        if (count!=size) {
            count+=1;
            array[count]=num;
            count+=1;
            return;
        }
        else {
        System.out.println("capacity is full");
        return;
        }

    }
    
    public int peek(){
        if (!this.isEmpty()) {
            return array[count];
        }
        else return -1;
    }
    
    public int pop(){
        if (!this.isEmpty()) {
            int last = array[count];
            count-=1;
            return last ;
        }
        else return -1;
    }
    }
    
    

    
    
