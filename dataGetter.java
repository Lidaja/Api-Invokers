import java.io.*;
import java.util.ArrayList;
import java.lang.Boolean;
public class dataGetter {
	public static ArrayList getData(Process p, String token){
		ArrayList<String> data = new ArrayList<String>();
		Boolean bool = false;
		String s = null;
		BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
		try{
			while((s = stdInput.readLine()) != null) {
				System.out.println(s);
				if (bool){
					data.add(s);
				}
				if (s.equals(token)){
					bool = !bool;
					if (!bool){
						data.remove(data.size()-1);
					}
				}
			}
		}catch(IOException e){
			System.out.println("IOException");
		}
		return data;
	}
}
