/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package calcengine;

/**
 *
 * @author josephleinwand
 */
public class CalcEngine {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        double val1 = 100.d;
        double val2 = 0.0d;
        double result;
        char opCode = 'a';
        
        if(opCode == 'd')
            result = val1 + val2;
        else if(opCode == 's')
            result = val1 - val2;
        else if(opCode == 'd')
            result = val2 != 0.0d ? val1 / val2 : 0.0d;
           // if(val2 != 0.0d)
            //    result  = val1 / val2;
           // else 
              //  result = 0.0d;
        else if(opCode == 'm')
            result = val1 * val2;
        else {
            System.out.println("Error - invalid opcode");
            result = 0.0d;
        }
        System.out.println(result);
    }
    
}
