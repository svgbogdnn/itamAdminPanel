import React, { ButtonHTMLAttributes } from 'react';
import * as Styled from './PrimaryButton.styled.ts';

type PrimaryButtonProps = {
  title: string;
};

export const PrimaryButton = ({ title }: ButtonHTMLAttributes<HTMLButtonElement> & PrimaryButtonProps) => {
  return (
    <Styled.Button>{title}</Styled.Button>
  );
};
