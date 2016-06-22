import java.io.*;

public class invokeData {
	public static void main(String args[]){
		try{
			Process p = Runtime.getRuntime().exec("./curlCaller.sh");
			printProcess.printData(p);
		}catch(IOException e){
			System.out.println("IOException");
		}
	}
}
