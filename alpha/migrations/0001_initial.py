# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Owner'
        db.create_table('alpha_owner', (
            ('user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('alpha', ['Owner'])

        # Adding model 'Person'
        db.create_table('alpha_person', (
            ('user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('alpha', ['Person'])

        # Adding model 'Article'
        db.create_table('alpha_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('alpha', ['Article'])

        # Adding model 'Entity'
        db.create_table('alpha_entity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alpha.Article'])),
            ('condition', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=4)),
        ))
        db.send_create_signal('alpha', ['Entity'])

        # Adding model 'Code'
        db.create_table('alpha_code', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alpha.Entity'])),
            ('family', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('alpha', ['Code'])

        # Adding model 'Loan'
        db.create_table('alpha_loan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alpha.Entity'])),
            ('fromPerson', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['alpha.Person'])),
            ('toPerson', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['alpha.Person'])),
            ('purpose', self.gf('django.db.models.fields.TextField')()),
            ('society', self.gf('django.db.models.fields.TextField')()),
            ('event', self.gf('django.db.models.fields.TextField')()),
            ('timeOrdered', self.gf('django.db.models.fields.DateField')()),
            ('timeFetched', self.gf('django.db.models.fields.DateField')()),
            ('timeExpired', self.gf('django.db.models.fields.DateField')()),
            ('timeReturned', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('alpha', ['Loan'])


    def backwards(self, orm):
        # Deleting model 'Owner'
        db.delete_table('alpha_owner')

        # Deleting model 'Person'
        db.delete_table('alpha_person')

        # Deleting model 'Article'
        db.delete_table('alpha_article')

        # Deleting model 'Entity'
        db.delete_table('alpha_entity')

        # Deleting model 'Code'
        db.delete_table('alpha_code')

        # Deleting model 'Loan'
        db.delete_table('alpha_loan')


    models = {
        'alpha.article': {
            'Meta': {'object_name': 'Article'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'alpha.code': {
            'Meta': {'object_name': 'Code'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alpha.Entity']"}),
            'family': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'alpha.entity': {
            'Meta': {'object_name': 'Entity'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alpha.Article']"}),
            'condition': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'alpha.loan': {
            'Meta': {'object_name': 'Loan'},
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alpha.Entity']"}),
            'event': ('django.db.models.fields.TextField', [], {}),
            'fromPerson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['alpha.Person']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.TextField', [], {}),
            'society': ('django.db.models.fields.TextField', [], {}),
            'timeExpired': ('django.db.models.fields.DateField', [], {}),
            'timeFetched': ('django.db.models.fields.DateField', [], {}),
            'timeOrdered': ('django.db.models.fields.DateField', [], {}),
            'timeReturned': ('django.db.models.fields.DateField', [], {}),
            'toPerson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['alpha.Person']"})
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