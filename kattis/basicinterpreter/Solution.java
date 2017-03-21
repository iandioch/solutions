import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Solution {

    static class ArithmeticStatement {}
    
    static class Operation {
        public Operation() {
        }

        public void run() {

        }

        public String toString() {
            return "hi";
        }
    }

    static class ShortLetOperation extends Operation {
        char var, c;
        String s;

        public ShortLetOperation(char var, String s) {
            this.var = var;
            this.s = s;
            this.c = getVariableName(s);
        }
    
        @Override public void run() {
            if (this.c == 0) {
                vartable[this.var] = Integer.parseInt(this.s);
            } else {
                vartable[this.var] = vartable[this.c];
            }
        }
    }

    static class LongLetOperation extends Operation {
        char var, op;
        String x, y;

        public LongLetOperation(char var, String x, char op, String y) {
            this.var = var;
            this.x = x;
            this.op = op;
            this.y = y;
        }

        @Override public void run() {
            //System.out.println("Long let: " + x + " " + op + " " + y);
            int a, b;
            char xn = getVariableName(this.x);
            char yn = getVariableName(this.y);
            if (xn == 0) {
                a = Integer.parseInt(x);
            } else {
                a = vartable[xn];
            }
            if (yn == 0) {
                b = Integer.parseInt(y);
            } else {
                b = vartable[yn];
            }
            int result = -1;
            switch (this.op) {
                case '*':
                    result = a*b;
                    break;
                case '/':
                    result = a/b;
                    break;
                case '+':
                    result = a+b;
                    break;
                case '-':
                    result = a-b;
            }
            vartable[this.var] = result;
        }
    }

    static class PrintOperation extends Operation {
        boolean newline;
        String statement;
        char var;

        public PrintOperation(boolean newline, String statement) {
            this.newline = newline;
            if (statement.charAt(0) == '"') {
                this.var = 0;
                this.statement = statement.substring(1, statement.length() - 1);
            } else {
                this.var = statement.charAt(0);
            }
        }

        @Override public void run() {
            if (this.var == 0) {
                System.out.print(this.statement);
            } else {
                System.out.print(vartable[this.var]);
            }
            if (this.newline) {
                System.out.println();
            }
        }
    }

    static class ConditionalOperation extends Operation {
        Integer dest;
        String x, op, y;

        public ConditionalOperation(Integer dest, String x, String op, String y) {
            this.dest = dest;
            this.x = x;
            this.op = op;
            this.y = y;
        }

        private boolean isTrue(int a, String op, int b) {
            if (op.equals("=")) return a==b;
            if (op.equals(">")) return a>b;
            if (op.equals("<")) return a<b;
            if (op.equals("<>")) return a!=b;
            if (op.equals("<=")) return a<=b;
            return a>=b;
        }

        @Override public void run() {
            //System.out.println("If " + x + " " + op + " " + y + " then go to " + dest);
            int a, b;
            char xn = getVariableName(this.x);
            char yn = getVariableName(this.y);
            if (xn == 0) {
                a = Integer.parseInt(x);
            } else {
                a = vartable[xn];
            }
            if (yn == 0) {
                b = Integer.parseInt(y);
            } else {
                b = vartable[yn];
            }
            if (isTrue(a, this.op, b)) {
                currLabel = dest-1;
            }
        }
    }


    static TreeMap<Integer, Operation> labelToOperation = new TreeMap<>();
    //static ArrayList<Integer> sortedLabels = new ArrayList<>();
    static Integer currLabel;
    static Operation currentOp;

    static int[] vartable = new int['Z'+1];

    public static char getVariableName(String s) {
        // returns 0 if not a valid var
        char c = s.charAt(0);
        if (c >= 'A' && c <= 'Z') {
            return c;
        }
        return 0;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        String[] parts;
        int label;
        String command;
        while (true) {
            line = in.readLine();
            if (line == null) {
                break;
            }
            parts = line.split("\\s+");
            label = Integer.parseInt(parts[0]);
            command = parts[1];

            Operation op = null;

            if (command.charAt(0) == 'L') {
                // LET
                char var = parts[2].charAt(0);
                if (parts.length == 5) {
                    op = new ShortLetOperation(var, parts[4]);
                } else {
                    op = new LongLetOperation(var, parts[4], parts[5].charAt(0), parts[6]);
                }
            } else if (command.charAt(0) == 'I') {
                int dest = Integer.parseInt(parts[parts.length-1]);
                // IF
                op = new ConditionalOperation(dest, parts[2], parts[3], parts[4]);
            } else {
                // PRINT or PRINTLN
                StringBuilder b = new StringBuilder(parts[2]);
                for (int i = 3; i < parts.length; i++) {
                    b.append(" ");
                    b.append(parts[i]);
                }
                op = new PrintOperation(command.length() > 5, b.toString());
            } 

            labelToOperation.put(label, op);
        }
        currLabel = labelToOperation.firstKey();
        while (true) {
            if (currLabel == null) {
                break;
            }
            labelToOperation.get(currLabel).run();
            currLabel = labelToOperation.higherKey(currLabel);
        }
    }
}
