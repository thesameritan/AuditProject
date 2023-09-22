import javax.swing.*;
import java.awt.*;

public class GUI {
        public static void clear(JPanel panel)
        {
            for (Component control : panel.getComponents())
            {
                if (control instanceof JTextField ctrl)
                {
                    ctrl.setText("");
                }
            }
        }

    public static void setFrame (JFrame frame, JPanel panel) {
        panel.setPreferredSize(new Dimension(700, 900));
        panel.setLayout(new GridLayout(19, 2, 10, 5));
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(panel);
        frame.pack();
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

}
