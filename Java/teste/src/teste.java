public class teste {
    public static void main(String[] args){
        System.out.print("Olá\n");

        String firstName = "Gabriel";
        String secondName = "Oliveira";
        String fullName = nome(firstName,secondName);
        System.out.print(fullName);
    }

    public static String nome(String firstName, String secondName){
        return "Nome Completo: " + firstName.concat(" ").concat(secondName);
    }

}

