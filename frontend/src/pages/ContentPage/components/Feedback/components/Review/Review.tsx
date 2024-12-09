import React from 'react';
import { TReview } from './Review.types';
import * as Styled from './Review.styled';
import { ActionButton } from '@src/components/ActionButton';

type ReviewProps = {
  review: TReview;
};

export const Review = ({ review }: ReviewProps) => {
  const { name, course, rating, comment, date } = review;

  return (
    <Styled.Container>
      <Styled.Header>
        <Styled.Group>
          <Styled.Field>{name}</Styled.Field>
          <Styled.Field>{`Курс: ${course}`}</Styled.Field>
        </Styled.Group>
        <Styled.Group>
          <Styled.Field>{`Оценка: ${rating}`}</Styled.Field>
        </Styled.Group>
      </Styled.Header>
      {!!comment && <Styled.Comment>{comment}</Styled.Comment>}
      <Styled.Footer>
        <Styled.Group>
          <Styled.Field>{`Дата: ${date}`}</Styled.Field>
        </Styled.Group>
        <Styled.Group>
          <ActionButton type='button' title='Скрыть' />
          <ActionButton type='button' title='Удалить' />
        </Styled.Group>
      </Styled.Footer>
    </Styled.Container>
  );
};
