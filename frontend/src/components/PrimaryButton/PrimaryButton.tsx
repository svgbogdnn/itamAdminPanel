import React, { ButtonHTMLAttributes } from 'react';
import * as Styled from './PrimaryButton.styled';

type PrimaryButtonProps = {
  title: string;
};

export const PrimaryButton = ({ title, ...props }: React.HTMLAttributes<HTMLElement> & ButtonHTMLAttributes<HTMLButtonElement> & PrimaryButtonProps) => {
  return (
    <Styled.Button {...props}>{title}</Styled.Button>
  );
};
