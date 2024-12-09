import React from 'react';
import * as Styled from './FilterField.styled';

type FilterFieldProps = {
  title: string;
};

export const FilterField = ({ title }: FilterFieldProps) => {
  return (
    <Styled.Container>
      <Styled.Title>{title}</Styled.Title>
      <Styled.Icon />
    </Styled.Container>
  );
};
