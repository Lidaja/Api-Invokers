import java.io.*;
import java.util.ArrayList;
import java.lang.Boolean;
public class printProcess {
	public static void printData(Process p){
		String s = null;
		String t = null;
		BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
		BufferedReader stdError = new BufferedReader(new InputStreamReader(p.getErrorStream()));
		try{
			while((s = stdInput.readLine()) != null) {
				System.out.println(s);
			}
			while((t = stdError.readLine()) != null) {
				System.out.println(t);
			}
		}catch(IOException e){
			System.out.println("IOException");
		}
	}
}
