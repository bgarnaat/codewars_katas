/*
Story

Due to lack of maintenance the minute-hand has fallen off Town Hall clock face.

And because the local council has lost most of our tax money to a Nigerian email scam there are no funds to fix the clock properly.

Instead, they are asking for volunteer programmers to write some code that tell the time by only looking at the remaining hour-hand!

What a bunch of cheap-skates!

Can you do it?

Kata

Given the angle (in degrees) of the hour-hand, return the time in HH:MM format. Round down to the nearest minute.

Examples

12:00 = 0 degrees
03:00 = 90 degrees
06:00 = 180 degrees
09:00 = 270 degrees
12:00 = 360 degrees
Notes

0 <= angle <= 360
*/


public class Dinglemouse {

  public static String whatTimeIsIt(final double angle) {
    String hour = "";
    if ((int)(angle / 30) == 0) {
      hour = "12";
    } else {
      hour = String.format("%2s", String.valueOf((int)(angle / 30))).replace(" ", "0");
    }
    String minute = String.format("%2s", String.valueOf((int)(angle % 30 * 2))).replace(" ", "0");
    return hour + ':' + minute;
  }

}


/*
BEST ANSWER:


import java.text.DecimalFormat;
public class Dinglemouse {
  public static String whatTimeIsIt(final double angle) {
    DecimalFormat df = new DecimalFormat("00");
    double time = (angle/.5)/60;
    int hours = (int) time;
    int minutes = (int) (time * 60) % 60;
    if(hours == 0){hours = 12;}
    return String.valueOf(df.format(hours))+":"+String.valueOf(df.format(minutes));
  }
}
*/
