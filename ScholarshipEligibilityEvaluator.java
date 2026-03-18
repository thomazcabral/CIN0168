import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class ScholarshipEligibilityEvaluator {

    public enum Status {
        APPROVED,
        REJECTED,
        MANUAL_REVIEW
    }

    public static class EvaluationResult {
        private final Status status;
        private final List<String> reasons;

        public EvaluationResult(Status status, List<String> reasons) {
            this.status = Objects.requireNonNull(status);
            this.reasons = List.copyOf(reasons);
        }

        public Status getStatus() {
            return status;
        }

        public List<String> getReasons() {
            return reasons;
        }

        @Override
        public String toString() {
            return "EvaluationResult{" +
                    "status=" + status +
                    ", reasons=" + reasons +
                    '}';
        }
    }

    public static EvaluationResult evaluateScholarship(
            int age,
            double gpa,
            double attendanceRate,
            boolean hasRequiredCourses,
            boolean disciplinaryRecord
    ) {
        validateInputs(gpa, attendanceRate);

        List<String> rejectionReasons = new ArrayList<>();
        List<String> reviewReasons = new ArrayList<>();

        // Rule 1 - Age
        if (age < 16) {
            rejectionReasons.add("Applicant is younger than the minimum age.");
        } else if (age <= 17) {
            reviewReasons.add("Applicant is under 18 and requires manual review.");
        }

        // Rule 2 - GPA
        if (gpa < 6.0) {
            rejectionReasons.add("GPA is below the minimum required.");
        } else if (gpa < 7.0) {
            reviewReasons.add("GPA is in the manual review range.");
        }

        // Rule 3 - Attendance
        if (attendanceRate < 75.0) {
            rejectionReasons.add("Attendance rate is below the minimum required.");
        } else if (attendanceRate < 80.0) {
            reviewReasons.add("Attendance rate is in the manual review range.");
        }

        // Rule 4 - Required courses
        if (!hasRequiredCourses) {
            rejectionReasons.add("Required courses have not been completed.");
        }

        // Rule 5 - Disciplinary record
        if (disciplinaryRecord) {
            rejectionReasons.add("Applicant has a disciplinary record.");
        }

        // Final decision
        if (!rejectionReasons.isEmpty()) {
            return new EvaluationResult(Status.REJECTED, rejectionReasons);
        }

        if (!reviewReasons.isEmpty()) {
            return new EvaluationResult(Status.MANUAL_REVIEW, reviewReasons);
        }

        return new EvaluationResult(Status.APPROVED, List.of("Applicant meets all scholarship requirements."));
    }

    private static void validateInputs(double gpa, double attendanceRate) {
        if (gpa < 0.0 || gpa > 10.0) {
            throw new IllegalArgumentException("GPA must be between 0 and 10.");
        }

        if (attendanceRate < 0.0 || attendanceRate > 100.0) {
            throw new IllegalArgumentException("Attendance rate must be between 0 and 100.");
        }
    }

    public static void main(String[] args) {
        EvaluationResult result = evaluateScholarship(
                18,
                8.5,
                92.0,
                true,
                false
        );

        System.out.println(result);
    }
}