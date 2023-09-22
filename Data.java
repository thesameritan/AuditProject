import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Array;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.Arrays;
import java.util.List;

@SuppressWarnings("unchecked")
public class Data {
    public static void processData(Patient patient) {
        JSONObject patientJsonObject = new JSONObject();
        JSONArray comorbidities = new JSONArray();


        patientJsonObject.put("Patient MRN", patient.getPatientMRN());
        patientJsonObject.put("Age", patient.getAge());
        comorbidities.addAll(Arrays.asList(patient.getComorbidities()));
        patientJsonObject.put("Patient Comorbidities", comorbidities);
        patientJsonObject.put("Dementia?", patient.getHasDementia());
        patientJsonObject.put("Date Admitted", patient.getAdmissionDateAndTime());
        patientJsonObject.put("Date Discharged", patient.getDischargeDateAndTime());
        patientJsonObject.put("Discharged to", patient.getDischargedTo());
        patientJsonObject.put("Mental Illness?", patient.getIsMentallyIll());
        patientJsonObject.put("Hours of RAAS <= -3", patient.getRaas());
        patientJsonObject.put("Days pain dealt with", Arrays.asList(patient.getDaysPainDealtWith()));
        patientJsonObject.put("Days Nursing Notes delirium +ve daytime", Arrays.asList(patient.getDaysNursingDeliriumDaytime()));
        patientJsonObject.put("Days Nursing Notes delirium +ve nighttime", Arrays.asList(patient.getDaysNursingDeliriumNightTime()));
        patientJsonObject.put("Days CAM ICU set to be done", Arrays.asList(patient.getDaysCAMICUToBeDone()));
        patientJsonObject.put("Patient Impairment", patient.getIsImpaired());
        patientJsonObject.put("Days CAM ICU +ve", Arrays.asList(patient.getDaysCAMICUPositive()));
        patientJsonObject.put("Days on meds", Arrays.asList(patient.getDaysOnMedication()));
        patientJsonObject.put("Patient Discharge Time", patient.getDischargeDateAndTime());
        patientJsonObject.put("Patient Discharged To", patient.getDischargedTo());

        try {
            final Path path = Paths.get("C:\\Users\\thesa\\Desktop\\auditProject\\Audit\\PatientData.json");
            Files.write(path, List.of(patientJsonObject.toString()
                    ), StandardCharsets.UTF_8,
                    Files.exists(path) ? StandardOpenOption.APPEND : StandardOpenOption.CREATE);
        } catch (final IOException ioe) {
            // Add your own exception handling...
        }


    }

    public static void rewriteData() {
        try (BufferedReader br = new BufferedReader(new FileReader("C:\\Users\\thesa\\Desktop\\auditProject\\Audit\\PatientData.json"))) {
            String line;
            while ((line = br.readLine()) != null) {
                JSONParser parser = new JSONParser();
                JSONObject json = (JSONObject) parser.parse(line);

                try {
                    final Path path = Paths.get("C:\\Users\\thesa\\Desktop\\auditProject\\Audit\\real.json");
                    Files.write(path, List.of(json.toString()
                            ), StandardCharsets.UTF_8,
                            Files.exists(path) ? StandardOpenOption.APPEND : StandardOpenOption.CREATE);
                } catch (final IOException ioe) {
                    // Add your own exception handling...
                }
            }
        } catch (IOException | ParseException e) {
            throw new RuntimeException(e);
        }
    }
}
