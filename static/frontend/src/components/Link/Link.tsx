import React from 'react';
import * as Styled from './Link.styled.ts';

type LinkProps = {
  title: string;
};

export const Link = ({ title }: LinkProps) => {
  return (
    <Styled.Text>{title}</Styled.Text>
  );
};
