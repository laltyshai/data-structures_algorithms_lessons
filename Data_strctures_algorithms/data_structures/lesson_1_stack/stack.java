/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
		System.out.println("Hello World");
	}
}

public class Stack {
    private int[] array;
    private int count;
    private int size;
    
    public Stack(int siz) {
        array = new int[siz];
        size = siz;
        count=0;
    }
    
    public void isEmpty() {
        if (count==o) return True;
        return False;
    }
    
    
    
    
    public void push(int num){
        if (count!=size) {
            count+=1;
            array[count]=num;
            count+=1;
            return;
        }
        else {
        system.out.println("capacity is full");
        return;
        }

    }
    
    public void peek(){
        
    }
    
    
    
    
    
    
    
    
}