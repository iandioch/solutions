import java.util.Set;
import java.util.HashSet;
import java.lang.Character;
import java.util.Arrays;

class Easy{

	private static Set<Character> vowels;

	private static char toUpper(char c){
		return Character.toUpperCase(c);
	}

	private static char toLower(char c){
		return Character.toLowerCase(c);
	}

	private static boolean isVowel(char c){
		return vowels.contains(toUpper(c));
	}

	private static boolean isPunctuation(int c){
		return !Character.isLetter(c);
	}

	private static String encode(String in){
		char[] chars = in.toCharArray();
		StringBuilder out = new StringBuilder(in.length());

		for(int i = 0; i < chars.length; i ++){
			if(isVowel(chars[i]) || isPunctuation(chars[i])){
				out.append(chars[i]);
			}else{
				out.append(chars[i]);
				out.append("o");
				out.append(toLower(chars[i]));
			}
		}
		return out.toString();
	}

	private static String decode(String in){
		char[] chars = in.toCharArray();
		boolean[] ignore = new boolean[chars.length];
		StringBuilder out = new StringBuilder(in.length()/2);

		for(int i = 0; i < chars.length; i ++){
			if(ignore[i]) continue;

			if(isVowel(chars[i]) || isPunctuation(chars[i])){
				out.append(chars[i]);
			}else{
				out.append(chars[i]);
				ignore[i+1] = true;
				ignore[i+2] = true;
			}
		}
		return out.toString();
	}

	public static void main(String[] args){
		vowels = new HashSet<Character>(Arrays.asList(new Character[]{'A', 'E', 'I', 'O', 'U', 'Y', 'Å', 'Ä', 'Ö'}));
		if(args[0].equals("-d") || args[0].equals("-decode")){
			System.out.println(decode(args[1]));
		}else if(args[0].equals("-e") || args[0].equals("-encode")){
			System.out.println(encode(args[1]));
		}else{
			System.out.println(encode(args[0]));
		}
	}
}