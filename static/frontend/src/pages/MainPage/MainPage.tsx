import React from 'react';
import { Content } from '../../components/Content';
import * as Styled from './MainPage.styled.ts';
import { PrimaryButton } from '../../components/PrimaryButton';

export const MainPage = () => {
  return (
    <Styled.Wrapper>
      <Styled.Title>ITAM</Styled.Title>
      <Content>
        <Styled.Container>
          <PrimaryButton type='button' title='Войти' />
          <PrimaryButton type='button' title='Зарегистрироваться' />
        </Styled.Container>
      </Content>
    </Styled.Wrapper>
  );
};
