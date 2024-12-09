import React from 'react';
import { Header } from '../../components/Header';
import { Content } from '../../components/Content';
import * as Styled from './RegisterPage.styled';
import { TextInput } from '../../components/TextInput';
import { PrimaryButton } from '../../components/PrimaryButton';
import { PrimaryCheckbox } from '../../components/PrimaryCheckbox';

export const RegisterPage = () => {
  return (
    <Styled.Container>
      <Header links={[{ title: 'Вернуться назад' }]} />
      <Content title='Регистрация' links={[{ title: 'Уже есть аккаунт? Войти' }]}>
        <Styled.Form autoComplete='off'>
          <TextInput id='name' placeholder='ФИО' autoComplete='off' />
          <TextInput id='email' placeholder='Номер телефона' autoComplete='off' isValid />
          <TextInput id='email' type='email' placeholder='Почта' autoComplete='off' />
          <TextInput id='password' type='password' placeholder='Пароль' autoComplete='off' />
          <TextInput id='password' type='password' placeholder='Повторите пароль' autoComplete='off' />
          <PrimaryCheckbox id='accept' name='accept' label='Согласен с политикой сайта' />
          <PrimaryButton type='submit' title='Зарегистрироваться' />
        </Styled.Form>
      </Content>
    </Styled.Container>
  );
};
