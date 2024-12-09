import React, { ButtonHTMLAttributes } from 'react';
import * as Styled from './ActionButton.styled';

type ActionButtonProps = {
  title: string;
};

export const ActionButton = ({ title }: ButtonHTMLAttributes<HTMLButtonElement> & ActionButtonProps) => {
  return (
    <Styled.Button>{title}</Styled.Button>
  );
};
