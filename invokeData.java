import java.io.*;

public class invokeData {
	public static void main(String args[]){
		try{
			Process p = Runtime.getRuntime().exec("curl --unix-socket /var/run/system-docker.sh -s -H \"Content-Type: application/json\" -X POST -d '{\"AttachStdin\": false, \"AttachStdout\": true, \"AttachStderr\": true, \"Tty\": false, \"Cmd\": [ $params ]}' http:/containers/$DENALI_SERVICE/exec | jq '.Id' | tr -d '\"'");
			//System.out.println(dataGetter.getData(p,"@*@"));
		}catch(IOException e){
			System.out.println("IOException");
		}
	}
}
