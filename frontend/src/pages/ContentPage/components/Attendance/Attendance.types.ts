export enum EAttendanceStatus {
  attend = 'attend',
  absent = 'absent',
}

export type AttendanceTableValue = {
  key: string;
  name: string;
  course: string;
  date: string;
  status: EAttendanceStatus;
};
