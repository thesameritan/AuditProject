import javax.swing.*;

public class Main {
    static Patient patient;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(Main::createWindow);
        Data.rewriteData();
    }

    public static void createWindow() {

        patient = new Patient();

        JFrame frame = new JFrame("Audit Project");
        JPanel mainPanel = new javax.swing.JPanel();

        //components
        JLabel patientMRNLabel = new JLabel("Enter Patient MRN");
        JTextField patientMRN = new JTextField();

        JLabel patientAgeLabel = new JLabel("Enter Patient Age");
        JTextField patientAge = new JTextField();

        JLabel patientLengthOfStayLabel = new JLabel("Enter Patient Admission Date and Time");
        JTextField patientLengthOfStay = new JTextField();

        JLabel patientDischargeTimeLabel = new JLabel("Enter Patient Discharge Date and Time");
        JTextField patientDischargeTime = new JTextField();

        JLabel patientDischargedToLabel = new JLabel("Enter Patient Discharged To");
        JTextField patientDischargedTo = new JTextField();

        JLabel patientComorbiditiesLabel = new JLabel("Enter Patient Hx/PMhx");
        JTextField patientComorbidities = new JTextField();

        JLabel patientIsMentallyIllLabel = new JLabel("Does patient has a hx of mental illness?");
        JTextField patientIsMentallyIll = new JTextField();


        JLabel patientHasDementiaLabel = new JLabel("Does patient have dementia?");
        JTextField patientHasDementia = new JTextField();

        JLabel patientFrailtyScoreLabel = new JLabel("Enter Patient Frailty Score");
        JTextField patientFrailtyScore = new JTextField();

        JLabel patientDaysOnMedicationLabel = new JLabel("Which days pt on LISTED AND OUTLINED medication?");
        JTextField patientDaysOnMedication = new JTextField();

        JLabel patientRaasLabel = new JLabel("How many hours was pt RASS <= -3?");
        JTextField patientRaas = new JTextField();

        JLabel patientPainManagementLabel = new JLabel("Enter amount of days pain has NOT been dealt with?");
        JTextField patientPainManagement = new JTextField();

        JLabel patientNursingDeliriumLabel = new JLabel("Which days where nursing notes indicated any sign of delirium during daytime");
        JTextField patientNursingDelirium = new JTextField();

        JLabel patientNursingDeliriumLabel2 = new JLabel("Which days where nursing notes indicated any sign of delirium in night?");
        JTextField patientNursingDelirium2 = new JTextField();

        JLabel patientCamDeliriumLabel = new JLabel("Which days where CAM-ICU was recorded +ve in a 12 hour shift"); //array of days
        JTextField patientCamDelirium = new JTextField();

        JLabel patientImpairedLabel = new JLabel("Patient visually or hearing impaired?");
        JTextField patientImpaired = new JTextField();

        JLabel patientCAMICUToBeDoneLabel = new JLabel("Which days where CAM-ICU is marked to be done in a 12 hour shift");
        JTextField patientCAMICUToBeDone = new JTextField();



        JButton confirmInput = new JButton("Confirm Input");

        confirmInput.addActionListener(e -> {
            patient.setPatientMRN(patientMRN.getText());
            patient.setAge(patientAge.getText());
            patient.setComorbidities(
                    patientComorbidities.getText().split(",")
            );

            patient.setDischargeDateAndTime(patientDischargeTime.getText());
            patient.setDischargedTo(patientDischargedTo.getText());
            patient.setAdmissionDateAndTime(patientLengthOfStay.getText());
            patient.setHasDementia(patientHasDementia.getText());
            patient.setIsMentallyIll(patientIsMentallyIll.getText());
            patient.setRaas(patientRaas.getText());

            patient.setDaysOnMedication(patientDaysOnMedication.getText().split(","));
            patient.setIsImpaired(patientImpaired.getText());
            patient.setDaysPainDealtWith(patientPainManagement.getText().split(","));

            //System.out.println(patientPainManagement.getText().split(",")); java returning object instead of string lol
            //System.out.println(Arrays.toString(patientPainManagement.getText().split(",")));
            patient.setDaysNursingDeliriumDaytime(patientNursingDelirium.getText().split(","));
            patient.setDaysNursingDeliriumNightTime(patientNursingDelirium2.getText().split(","));
            patient.setDaysCAMICUToBeDone(patientCAMICUToBeDone.getText().split(","));
            patient.setDaysCAMICUPositive(patientCamDelirium.getText().split(","));


            System.out.println(patient.getPatientMRN());
            Data.processData(patient);
            GUI.clear(mainPanel);
        });


        mainPanel.add(patientMRNLabel);
        mainPanel.add(patientMRN);
        mainPanel.add(patientAgeLabel);
        mainPanel.add(patientAge);
        mainPanel.add(patientLengthOfStayLabel);
        mainPanel.add(patientLengthOfStay);
        mainPanel.add(patientDischargeTimeLabel);
        mainPanel.add(patientDischargeTime);
        mainPanel.add(patientDischargedToLabel);
        mainPanel.add(patientDischargedTo);
        mainPanel.add(patientComorbiditiesLabel);
        mainPanel.add(patientComorbidities);
        mainPanel.add(patientIsMentallyIllLabel);
        mainPanel.add(patientIsMentallyIll);
        mainPanel.add(patientHasDementiaLabel);
        mainPanel.add(patientHasDementia);
        mainPanel.add(patientFrailtyScoreLabel);
        mainPanel.add(patientFrailtyScore);
        mainPanel.add(patientDaysOnMedicationLabel);
        mainPanel.add(patientDaysOnMedication);
        mainPanel.add(patientRaasLabel);
        mainPanel.add(patientRaas);
        mainPanel.add(patientImpairedLabel);
        mainPanel.add(patientImpaired);
        mainPanel.add(patientPainManagementLabel);
        mainPanel.add(patientPainManagement);
        mainPanel.add(patientNursingDeliriumLabel);
        mainPanel.add(patientNursingDelirium);
        mainPanel.add(patientNursingDeliriumLabel2);
        mainPanel.add(patientNursingDelirium2);
        mainPanel.add(patientCamDeliriumLabel);
        mainPanel.add(patientCamDelirium);
        mainPanel.add(patientCAMICUToBeDoneLabel);
        mainPanel.add(patientCAMICUToBeDone);


        mainPanel.add(confirmInput);

        //frame finalisation
        GUI.setFrame(frame, mainPanel);
    }
}