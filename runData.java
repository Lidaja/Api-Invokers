import java.io.*;

public class runData {
	public static void main(String args[]){
		try{
			Process p = Runtime.getRuntime().exec("python generateData.py");
			System.out.println(dataGetter.getData(p,"@*@"));
		}catch(IOException e){
			System.out.println("IOException");
		}
	}
}
