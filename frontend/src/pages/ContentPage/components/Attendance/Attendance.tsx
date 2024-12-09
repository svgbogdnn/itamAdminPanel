import { Container } from '@src/components/Container';
import { FilterPanel } from '@src/components/FilterPanel';
import React from 'react'
import * as Styled from './Attendance.styled';
import { SecondaryButton } from '@src/components/SecondaryButton';
import { PrimaryTable } from '@src/components/PrimaryTable';
import { columns, filterFields, tableValues } from './Attendance.constants';

export const Attendance = () => {
  return (
    <Container>
      <FilterPanel fields={filterFields} />
      <Styled.Buttons>
        <SecondaryButton title='Отметить всех присутствующими' />
        <SecondaryButton title='Отметить всех отсутствующими' />
      </Styled.Buttons>
      <PrimaryTable data={tableValues} columns={columns} />
    </Container>
  );
};
