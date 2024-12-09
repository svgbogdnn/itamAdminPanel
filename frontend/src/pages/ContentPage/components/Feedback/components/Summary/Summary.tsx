import React from 'react';
import * as Styled from './Summary.styled';

type SummaryProps = {
  course: string;
  averageRating: string;
  commentsCount: string;
};

export const Summary = ({course, averageRating, commentsCount}: SummaryProps) => {
  return (
    <Styled.Container>
      <Styled.Group>
        <Styled.Field>{`Курс: ${course}`}</Styled.Field>
        <Styled.Field>{`Средняя оценка: ${averageRating}`}</Styled.Field>
      </Styled.Group>
      <Styled.Group>
        <Styled.Field>{`Количество комментариев: ${commentsCount}`}</Styled.Field>
      </Styled.Group>
    </Styled.Container>
  )
}