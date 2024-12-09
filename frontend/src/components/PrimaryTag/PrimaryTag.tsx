import React from 'react';
import * as Styled from './PrimaryTag.styled';

type PrimaryTagProps = {
  title: string;
  bgColor?: string;
};

export const PrimaryTag = ({ title, bgColor }: PrimaryTagProps) => {
  return (
    <Styled.Container $bgColor={bgColor ?? '#00B69B'}>{title}</Styled.Container>
  );
};
