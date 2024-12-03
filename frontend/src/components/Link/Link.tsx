import React from 'react';
import * as Styled from './Link.styled';

type LinkProps = {
  title: string;
};

export const Link = ({ title }: LinkProps) => {
  return (
    <Styled.Text>{title}</Styled.Text>
  );
};
