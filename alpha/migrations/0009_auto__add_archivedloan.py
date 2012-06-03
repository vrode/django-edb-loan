# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ArchivedLoan'
        db.create_table('alpha_archivedloan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alpha.Entity'], unique=True)),
            ('fromPerson', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['auth.User'])),
            ('toPerson', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['auth.User'])),
            ('society', self.gf('django.db.models.fields.TextField')()),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('event', self.gf('django.db.models.fields.TextField')()),
            ('timeFetched', self.gf('django.db.models.fields.DateField')()),
            ('timeExpired', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('alpha', ['ArchivedLoan'])


    def backwards(self, orm):
        # Deleting model 'ArchivedLoan'
        db.delete_table('alpha_archivedloan')


    models = {
        'alpha.archivedloan': {
            'Meta': {'object_name': 'ArchivedLoan'},
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alpha.Entity']", 'unique': 'True'}),
            'event': ('django.db.models.fields.TextField', [], {}),
            'fromPerson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'society': ('django.db.models.fields.TextField', [], {}),
            'timeExpired': ('django.db.models.fields.DateField', [], {}),
            'timeFetched': ('django.db.models.fields.DateField', [], {}),
            'toPerson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['auth.User']"})
        },
        'alpha.article': {
            'Meta': {'object_name': 'Article'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        'alpha.code': {
            'Meta': {'object_name': 'Code'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alpha.Entity']"}),
            'family': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'alpha.entity': {
            'Meta': {'object_name': 'Entity'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alpha.Article']"}),
            'condition': ('django.db.models.fields.DecimalField', [], {'default': "'1.0'", 'max_digits': '5', 'decimal_places': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'alpha.loan': {
            'Meta': {'object_name': 'Loan'},
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alpha.Entity']", 'unique': 'True'}),
            'event': ('django.db.models.fields.TextField', [], {}),
            'fromPerson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'society': ('django.db.models.fields.TextField', [], {}),
            'timeExpired': ('django.db.models.fields.DateField', [], {}),
            'timeFetched': ('django.db.models.fields.DateField', [], {}),
            'toPerson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['auth.User']"})
        },
        'alpha.owner': {
            'Meta': {'object_name': 'Owner', '_ormbases': ['auth.User']},
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'alpha.person': {
            'Meta': {'object_name': 'Person', '_ormbases': ['auth.User']},
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['alpha']