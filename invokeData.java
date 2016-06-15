import java.io.*;

public class invokeData {
	public static void main(String args[]){
		try{
			Process p = Runtime.getRuntime().exec("curl -v --unix-socket /var/run/system-docker.sock -H \"Content-Type: application/json\" -X POST -d \'{\"AttachStdin\": false, \"AttachStdout\": true, \"AttachStderr\": true, \"Tty\": false, \"Cmd\": [ \"ls\" ]}\' http:/containers/console/exec");
			//Process p = Runtime.getRuntime().exec("curl -v --unix-socket /var/run/system-docker.sock -H \"Content-Type: application/json\" -X POST -d '{\"AttachStdin\": false, \"AttachStdout\": true, \"AttachStderr\": true, \"Tty\": false, \"Cmd\": [ \"ls\" ]}' http:/containers/console/exec");
			printProcess.printData(p);
		}catch(IOException e){
			System.out.println("IOException");
		}
	}
}
