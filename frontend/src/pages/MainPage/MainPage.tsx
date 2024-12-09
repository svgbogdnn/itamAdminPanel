// import React from 'react';
import { Content } from '../../components/Content';
import * as Styled from './MainPage.styled';
import { PrimaryButton } from '../../components/PrimaryButton';
import { useNavigate } from 'react-router-dom';

export const MainPage = () => {
  const navigate = useNavigate();
  return (
    <Styled.Wrapper>
      <Styled.Title>ITAM</Styled.Title>
      <Content>
        <Styled.Container>
          <PrimaryButton type='button' title='Войти' onClick={() => {navigate('/login')}}/>
          <PrimaryButton type='button' title='Зарегистрироваться' onClick={() => navigate('/singin')}/>
        </Styled.Container>
      </Content>
    </Styled.Wrapper>
  );
};
