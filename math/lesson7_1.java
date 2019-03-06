import java.util.ArrayList;
import java.util.Arrays; 
import java.util.HashMap;

public class lesson7_1 {
	
	static char[] pwdcs = new char[]{'a','b','c','d','e'};
	static String[] crack(int len){
	String[] ps = new String[]{""};
		while (len -- > 0 ) {
			String[] nps = new String[ps.length * pwdcs.length];
			int nsbsi = 0;
			for(String pwd : ps){
				for(char c: pwdcs){
					nps[nsbsi ++] = pwd+c;
				}
			}
			ps = nps;
		}
		return ps;
	}
	public static void main(String[] args) {
		System.out.println("hello world");
		String[] pwds = crack(4);
		System.out.println(pwds.length);
		for(String pwd:pwds){
			System.out.println(pwd);
		}
	
	}
}
 
