import { EAttendanceStatus } from "../../Attendance.types";

export const mapAttendanceStatus = new Map<EAttendanceStatus, string>([
  [EAttendanceStatus.attend, 'Присутствовал'],
  [EAttendanceStatus.absent, 'Отсутствовал'],
]);

export const mapAttendanceStatusColor = new Map<EAttendanceStatus, string>([
  [EAttendanceStatus.attend, '#00B69B'],
  [EAttendanceStatus.absent, '#FF8743'],
]);
