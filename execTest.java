import java.io.*;

public class execTest {
	public static void main(String args[]){
		System.out.println("Java Test");
		String s = null;
		try{
			Process p = Runtime.getRuntime().exec("cd");
			BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
			while((s = stdInput.readLine()) != null) {
				System.out.println(s);
			}
		}catch (IOException e){
			System.out.println("Exception Happened");
		}		

	}
}
