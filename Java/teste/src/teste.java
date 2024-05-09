public class teste {
    public static void main(String[] args){
        System.out.print("Olá\n");

        String firstName = "Gabriel";
        String secondName = "Oliveira";
        String nomeCompleto = nome(firstName,secondName);
        System.out.print(nomeCompleto);
    }
    public static String nome(String firstName, String secondName){
        return "Nome Completo: " + firstName.concat(" ").concat(secondName);
    }   
}
