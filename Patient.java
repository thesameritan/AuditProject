public class Patient {
    String patientMRN;
    String age;
    String admissionDateAndTime;
    String dischargeDateAndTime;
    String dischargedTo;
    String isMentallyIll;
    String hasDementia;
    String raas; //how often is RAAS <-3 in patient stay?
    String[] daysOnMedication;
    String[] comorbidities; //split then search in array
    String[] daysPainDealtWith;
    String[] daysNursingDeliriumDaytime;
    String[] daysNursingDeliriumNightTime;
    String[] daysCAMICUPositive;
    String[] daysCAMICUToBeDone;
    String isImpaired; //Yes,Yes (yes is, yes something has been done?

    public String getDischargeDateAndTime() {
        return dischargeDateAndTime;
    }

    public void setDischargeDateAndTime(String dischargeDateAndTime) {
        this.dischargeDateAndTime = dischargeDateAndTime;
    }

    public String getDischargedTo() {
        return dischargedTo;
    }

    public void setDischargedTo(String dischargedTo) {
        this.dischargedTo = dischargedTo;
    }

    public String getPatientMRN() {
        return patientMRN;
    }

    public void setPatientMRN(String patientMRN) {
        this.patientMRN = patientMRN;
    }

    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public String getAdmissionDateAndTime() {
        return admissionDateAndTime;
    }

    public void setAdmissionDateAndTime(String admissionDateAndTime) {
        this.admissionDateAndTime = admissionDateAndTime;
    }

    public String[] getComorbidities() {
        return comorbidities;
    }

    public void setComorbidities(String[] comorbidities) {
        this.comorbidities = comorbidities;
    }

    public String getIsMentallyIll() {
        return isMentallyIll;
    }

    public void setIsMentallyIll(String isMentallyIll) {
        this.isMentallyIll = isMentallyIll;
    }

    public String getHasDementia() {
        return hasDementia;
    }

    public void setHasDementia(String hasDementia) {
        this.hasDementia = hasDementia;
    }

    public String getRaas() {
        return raas;
    }

    public void setRaas(String raas) {
        this.raas = raas;
    }

    public String[] getDaysOnMedication() {
        return daysOnMedication;
    }

    public void setDaysOnMedication(String[] daysOnMedication) {
        this.daysOnMedication = daysOnMedication;
    }

    public String[] getDaysPainDealtWith() {
        return daysPainDealtWith;
    }

    public void setDaysPainDealtWith(String[] daysPainDealtWith) {
        this.daysPainDealtWith = daysPainDealtWith;
    }

    public String[] getDaysNursingDeliriumDaytime() {
        return daysNursingDeliriumDaytime;
    }

    public void setDaysNursingDeliriumDaytime(String[] daysNursingDeliriumDaytime) {
        this.daysNursingDeliriumDaytime = daysNursingDeliriumDaytime;
    }

    public String[] getDaysNursingDeliriumNightTime() {
        return daysNursingDeliriumNightTime;
    }

    public void setDaysNursingDeliriumNightTime(String[] daysNursingDeliriumNightTime) {
        this.daysNursingDeliriumNightTime = daysNursingDeliriumNightTime;
    }

    public String[] getDaysCAMICUPositive() {
        return daysCAMICUPositive;
    }

    public void setDaysCAMICUPositive(String[] daysCAMICUPositive) {
        this.daysCAMICUPositive = daysCAMICUPositive;
    }

    public String[] getDaysCAMICUToBeDone() {
        return daysCAMICUToBeDone;
    }

    public void setDaysCAMICUToBeDone(String[] daysCAMICUToBeDone) {
        this.daysCAMICUToBeDone = daysCAMICUToBeDone;
    }

    public String getIsImpaired() {
        return isImpaired;
    }

    public void setIsImpaired(String isImpaired) {
        this.isImpaired = isImpaired;

    }
}