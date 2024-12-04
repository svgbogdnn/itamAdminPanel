import React from 'react';
import * as Styled from './Header.styled.ts';
import { Link } from '../Link';
import { HeaderLink } from '../../types.ts';

type HeaderProps = {
  links?: HeaderLink[];
};

export const Header = ({ links }: HeaderProps) => {
  return (
    <Styled.Container>
      <Styled.Nav>
        <Styled.Title>Itam</Styled.Title>
      </Styled.Nav>
      {!!links?.length && <Styled.Links>
        {links.map(({ title }) => (<Link key='title' title={title} />))}
      </Styled.Links>}
    </Styled.Container>
  );
};
