public class SmartTv {
    boolean power = false;
    int channel = 1;
    int volume = 0;

    public void powerOn(){
        power = true;
    }

    public void powerOff(){
        power = false;
    }

    public void moreVolume(){
        volume++;
    }

    public void lessVolume(){
        volume--;
    }

    public void changeChannel(int newChannel){
        channel = newChannel;
    }

    public void upChannel(){
        channel++;
    }

    public void lowChannel(){
        channel--;
    }
}
