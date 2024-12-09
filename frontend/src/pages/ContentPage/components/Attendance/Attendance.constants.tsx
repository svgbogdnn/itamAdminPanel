import { TFilterField } from "@src/components/FilterPanel/components/FilterField.types";
import { AttendanceTableValue, EAttendanceStatus } from "./Attendance.types";
import { TableProps } from "antd";
import { AttendanceStatus } from "./components/AttendanceStatus";

export const filterFields: TFilterField[] = [
  { title: 'Дата' },
  { title: 'Курс' },
  { title: 'Статус занятия' },
];

export const columns: TableProps<AttendanceTableValue>['columns'] = [
  {
    title: 'ФИО',
    dataIndex: 'name',
    key: 'name',
    align: 'center',
  },
  {
    title: 'Курс',
    dataIndex: 'course',
    key: 'course',
    align: 'center',
  },
  {
    title: 'Дата',
    dataIndex: 'date',
    key: 'date',
    align: 'center',
  },
  {
    title: 'Статус занятия',
    key: 'status',
    dataIndex: 'status',
    align: 'center',
    render: (_, { status }) => <AttendanceStatus status={status} />,
  },
];

export const tableValues: AttendanceTableValue[] = [
  {
    key: '1',
    name: 'Иванов Иван Иванович',
    course: 'Frontend PRO',
    date: '04 Sep 2019',
    status: EAttendanceStatus.attend,
  },
  {
    key: '2',
    name: 'Иванов Иван Иванович',
    course: 'Frontend PRO',
    date: '04 Sep 2019',
    status: EAttendanceStatus.absent,
  },
  {
    key: '3',
    name: 'Иванов Иван Иванович',
    course: 'Frontend PRO',
    date: '04 Sep 2019',
    status: EAttendanceStatus.attend,
  },
  {
    key: '4',
    name: 'Иванов Иван Иванович',
    course: 'Frontend PRO',
    date: '04 Sep 2019',
    status: EAttendanceStatus.attend,
  },
  {
    key: '5',
    name: 'Иванов Иван Иванович',
    course: 'Frontend PRO',
    date: '04 Sep 2019',
    status: EAttendanceStatus.attend,
  },
  {
    key: '6',
    name: 'Иванов Иван Иванович',
    course: 'Frontend PRO',
    date: '04 Sep 2019',
    status: EAttendanceStatus.absent,
  },
  {
    key: '7',
    name: 'Иванов Иван Иванович',
    course: 'Frontend PRO',
    date: '04 Sep 2019',
    status: EAttendanceStatus.attend,
  },
  {
    key: '8',
    name: 'Иванов Иван Иванович',
    course: 'Frontend PRO',
    date: '04 Sep 2019',
    status: EAttendanceStatus.attend,
  },
  {
    key: '9',
    name: 'Иванов Иван Иванович',
    course: 'Frontend PRO',
    date: '04 Sep 2019',
    status: EAttendanceStatus.absent,
  },
  {
    key: '10',
    name: 'Иванов Иван Иванович',
    course: 'Frontend PRO',
    date: '04 Sep 2019',
    status: EAttendanceStatus.attend,
  },
  {
    key: '11',
    name: 'Иванов Иван Иванович',
    course: 'Frontend PRO',
    date: '04 Sep 2019',
    status: EAttendanceStatus.attend,
  },
  {
    key: '12',
    name: 'Иванов Иван Иванович',
    course: 'Frontend PRO',
    date: '04 Sep 2019',
    status: EAttendanceStatus.attend,
  },
  {
    key: '13',
    name: 'Иванов Иван Иванович',
    course: 'Frontend PRO',
    date: '04 Sep 2019',
    status: EAttendanceStatus.absent,
  },
  {
    key: '14',
    name: 'Иванов Иван Иванович',
    course: 'Frontend PRO',
    date: '04 Sep 2019',
    status: EAttendanceStatus.attend,
  },
];
