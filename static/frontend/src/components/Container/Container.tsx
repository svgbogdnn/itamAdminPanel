import React, { PropsWithChildren } from 'react';
import * as Styled from './Container.styled.ts';

export const Container = ({ children }: PropsWithChildren) => {
  return (
    <Styled.Container>{children}</Styled.Container>
  );
};
