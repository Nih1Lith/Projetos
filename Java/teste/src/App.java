public class App {
    public static void main(String[] args) throws Exception {
        SmartTv smartTv = new SmartTv();

        System.out.println("Tv ligada? " + smartTv.power);

        System.out.println("Canal atual: " + smartTv.channel);

        System.out.println("Volume: " + smartTv.volume);

        smartTv.powerOn();
        
        System.out.println("Tv ligada: " + smartTv.power);
        
        smartTv.changeChannel(1);

        System.out.print("Canal Atual: " + smartTv.channel);
    }
}
