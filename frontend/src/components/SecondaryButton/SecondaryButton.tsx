import React from 'react';
import * as Styled from './SecondaryButton.styled';

type SecondaryButtonProps = {
  title: string;
};

export const SecondaryButton = ({ title }: SecondaryButtonProps) => {
  return (
    <Styled.Button>{title}</Styled.Button>
  );
};
