import React, { PropsWithChildren } from 'react';
import { HeaderLink } from '../../types';
import * as Styled from './Content.styled';
import { Link } from '../Link';

type ContentProps = {
  title?: string;
  links?: HeaderLink[];
};

export const Content = ({ title, links, children }: PropsWithChildren<ContentProps>) => {
  return (
    <Styled.Container>
      <Styled.FormContainer>
        {!!title && <Styled.Title>{title}</Styled.Title>}
        {children}
      </Styled.FormContainer>
      {!!links?.length && <Styled.Links>
        {links.map(({ title }) => <Link key={title} title={title} />)}
      </Styled.Links>}
    </Styled.Container>
  );
};
