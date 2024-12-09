import React from 'react';
import { EAttendanceStatus } from '../../Attendance.types';
import { PrimaryTag } from '@src/components/PrimaryTag';
import { mapAttendanceStatus, mapAttendanceStatusColor } from './AttendanceStatus.constants';
import * as Styled from './AttendanceStatus.styled';

type AttendanceStatusProps = {
  status: EAttendanceStatus;
};

export const AttendanceStatus = ({ status }: AttendanceStatusProps) => {
  return (
    <Styled.Container>
      <PrimaryTag title={mapAttendanceStatus.get(status) ?? ''} bgColor={mapAttendanceStatusColor.get(status)} />
      <Styled.EditIcon />
    </Styled.Container>
  );
};
